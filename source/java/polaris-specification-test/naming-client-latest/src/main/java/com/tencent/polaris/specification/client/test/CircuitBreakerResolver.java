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

package com.tencent.polaris.specification.client.test;

import java.util.concurrent.CountDownLatch;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.dataformat.yaml.YAMLMapper;
import com.google.protobuf.StringValue;
import com.google.protobuf.util.JsonFormat;
import com.tencent.polaris.specification.api.v1.fault.tolerance.CircuitBreakerProto;
import com.tencent.polaris.specification.api.v1.service.manage.PolarisGRPCGrpc;
import com.tencent.polaris.specification.api.v1.service.manage.RequestProto;
import com.tencent.polaris.specification.api.v1.service.manage.ResponseProto;
import com.tencent.polaris.specification.api.v1.service.manage.ServiceProto;
import io.grpc.stub.StreamObserver;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import static com.tencent.polaris.specification.api.v1.model.CodeProto.Code.ExecuteSuccess_VALUE;

public class CircuitBreakerResolver {

	private static final Logger LOG = LoggerFactory.getLogger(CircuitBreakerResolver.class);

	private static final RequestProto.DiscoverRequest.DiscoverRequestType REQUEST_TYPE =
			RequestProto.DiscoverRequest.DiscoverRequestType.CIRCUIT_BREAKER;

	private final PolarisGRPCGrpc.PolarisGRPCStub namingStub;

	public CircuitBreakerResolver(PolarisGRPCGrpc.PolarisGRPCStub namingStub) {
		this.namingStub = namingStub;
	}

	public void resolve() {
		CountDownLatch countDownLatch = new CountDownLatch(1);
		StreamObserver<RequestProto.DiscoverRequest> discoverClient = namingStub
				.discover(new StreamObserver<ResponseProto.DiscoverResponse>() {
					@Override
					public void onNext(ResponseProto.DiscoverResponse value) {
						int code = value.getCode().getValue();
						if (code != ExecuteSuccess_VALUE) {
							LOG.info("fail to pull resource for event type {}, result {}",
									REQUEST_TYPE, code);
							return;
						}
						CircuitBreakerProto.CircuitBreaker message = value.getCircuitBreaker();
						JsonFormat.Printer printer = JsonFormat.printer();
						String jsonStr = null;
						try {
							jsonStr = printer.print(message);
							JsonNode jsonNodeTree = new ObjectMapper().readTree(jsonStr);
							String jsonAsYaml = new YAMLMapper().writeValueAsString(jsonNodeTree);
							LOG.info("success to pull resource for event type {}, value {}", REQUEST_TYPE, jsonAsYaml);
						}
						catch (Exception e) {
							LOG.error("fail to print message for type {}", REQUEST_TYPE, e);
						}
						countDownLatch.countDown();
					}

					@Override
					public void onError(Throwable t) {
						countDownLatch.countDown();
						LOG.warn("fail to pull resource for type {}", REQUEST_TYPE, t);
					}

					@Override
					public void onCompleted() {
						countDownLatch.countDown();
					}
				});
		RequestProto.DiscoverRequest.Builder req = RequestProto.DiscoverRequest.newBuilder();
		req.setType(REQUEST_TYPE);
		req.setService(ServiceProto.Service.newBuilder().setNamespace(
				StringValue.newBuilder().setValue("Test").build()).setName(
						StringValue.newBuilder().setValue("TestSvc").build()).build());
		discoverClient.onNext(req.build());
		try {
			countDownLatch.await();
		} catch (InterruptedException e) {
			LOG.error("[ServerConnector] fail to wait check event type {}", REQUEST_TYPE, e);
		}
	}
}
