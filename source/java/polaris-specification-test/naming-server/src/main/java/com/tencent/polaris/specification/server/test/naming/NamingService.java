/*
 * Tencent is pleased to support the open source community by making Polaris available.
 *
 * Copyright (C) 2019 THL A29 Limited, a Tencent company. All rights reserved.
 *
 * Licensed under the BSD 3-Clause License (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * https://opensource.org/licenses/BSD-3-Clause
 *
 * Unless required by applicable law or agreed to in writing, software distributed
 * under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
 * CONDITIONS OF ANY KIND, either express or implied. See the License for the
 * specific language governing permissions and limitations under the License.
 */

package com.tencent.polaris.specification.server.test.naming;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.function.Function;

import com.google.common.cache.Cache;
import com.google.common.cache.CacheBuilder;
import com.google.protobuf.StringValue;
import com.google.protobuf.UInt32Value;
import com.tencent.polaris.specification.api.v1.model.CodeProto;
import com.tencent.polaris.specification.api.v1.service.manage.PolarisGRPCGrpc;
import com.tencent.polaris.specification.api.v1.service.manage.RequestProto;
import com.tencent.polaris.specification.api.v1.service.manage.ResponseProto;
import com.tencent.polaris.specification.api.v1.service.manage.ServiceProto;
import io.grpc.stub.StreamObserver;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class NamingService extends PolarisGRPCGrpc.PolarisGRPCImplBase {

	private static final Logger LOG = LoggerFactory.getLogger(NamingService.class);

	private final Map<RequestProto.DiscoverRequest.DiscoverRequestType, Cache<ServiceKey, ResponseProto.DiscoverResponse>> discoverResponses = new ConcurrentHashMap<>();

	public void putDiscoverResponse(RequestProto.DiscoverRequest.DiscoverRequestType discoverRequestType, ResponseProto.DiscoverResponse discoverResponse) {
		Cache<ServiceKey, ResponseProto.DiscoverResponse> serviceKeyDiscoverResponseCache = discoverResponses.computeIfAbsent(discoverRequestType, new Function<RequestProto.DiscoverRequest.DiscoverRequestType, Cache<ServiceKey, ResponseProto.DiscoverResponse>>() {
			@Override
			public Cache<ServiceKey, ResponseProto.DiscoverResponse> apply(RequestProto.DiscoverRequest.DiscoverRequestType discoverRequestType) {
				return CacheBuilder.newBuilder().build();
			}
		});
		ServiceKey serviceKey = new ServiceKey(discoverResponse.getService().getNamespace()
				.getValue(), discoverResponse.getService().getName().getValue());
		serviceKeyDiscoverResponseCache.put(serviceKey, discoverResponse);
	}

	@Override
	public StreamObserver<RequestProto.DiscoverRequest> discover(StreamObserver<ResponseProto.DiscoverResponse> responseObserver) {
		return new StreamObserver<RequestProto.DiscoverRequest>() {

			@Override
			public void onNext(RequestProto.DiscoverRequest req) {
				LOG.info("receive discover request {}", req);
				Cache<ServiceKey, ResponseProto.DiscoverResponse> serviceKeyDiscoverResponseCache = discoverResponses.get(req.getType());
				ResponseProto.DiscoverResponse discoverResponse = null;
				ServiceProto.Service service = req.getService();
				ServiceKey serviceKey = new ServiceKey(service.getNamespace().getValue(), service.getName().getValue());
				if (null != serviceKeyDiscoverResponseCache) {
					discoverResponse = serviceKeyDiscoverResponseCache.getIfPresent(serviceKey);
				}
				if (null == discoverResponse) {
					discoverResponse = buildServiceResponse(CodeProto.Code.NotFoundResource_VALUE,
							String.format("service %s not found", serviceKey));
					LOG.info("send discover not found response {}", discoverResponse);
					responseObserver.onNext(discoverResponse);
					return;
				}
				LOG.info("send discover response {}", discoverResponse);
				responseObserver.onNext(discoverResponse);
			}

			@Override
			public void onError(Throwable t) {
				LOG.error("receive client error", t);
			}

			@Override
			public void onCompleted() {
				responseObserver.onCompleted();
			}
		};
	}

	private ResponseProto.DiscoverResponse buildServiceResponse(int code, String info) {
		ResponseProto.DiscoverResponse.Builder builder = ResponseProto.DiscoverResponse.newBuilder();
		builder.setCode(UInt32Value.newBuilder().setValue(code).build());
		builder.setInfo(StringValue.newBuilder().setValue(info).build());
		return builder.build();
	}
}
