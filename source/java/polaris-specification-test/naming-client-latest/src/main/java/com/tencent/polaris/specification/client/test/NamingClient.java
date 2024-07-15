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

import com.tencent.polaris.specification.api.v1.service.manage.PolarisGRPCGrpc;
import io.grpc.ManagedChannelBuilder;

public class NamingClient {

	private static final String SERVER_HOST = "127.0.0.1";

	private static final int PORT = 18770;

	public static void main(String[] args) {
		PolarisGRPCGrpc.PolarisGRPCStub namingStub = PolarisGRPCGrpc.newStub(ManagedChannelBuilder.forAddress(SERVER_HOST, PORT)
				.usePlaintext().build());
		CircuitBreakerResolver circuitBreakerResolver = new CircuitBreakerResolver(namingStub);
		circuitBreakerResolver.resolve();
	}
}
