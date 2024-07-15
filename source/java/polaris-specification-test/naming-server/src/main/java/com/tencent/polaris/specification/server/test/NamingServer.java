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

package com.tencent.polaris.specification.server.test;

import java.util.concurrent.TimeUnit;

import com.tencent.polaris.specification.api.v1.service.manage.RequestProto;
import com.tencent.polaris.specification.server.test.builder.CircuitBreakerBuilder;
import com.tencent.polaris.specification.server.test.naming.NamingService;
import io.grpc.Grpc;
import io.grpc.InsecureServerCredentials;
import io.grpc.Server;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class NamingServer {

	private static final Logger LOG = LoggerFactory.getLogger(NamingServer.class);

	public static final int PORT = 18770;

	public static void main(String[] args) throws Exception {
		NamingService namingService = new NamingService();
		namingService.putDiscoverResponse(RequestProto.DiscoverRequest.DiscoverRequestType.CIRCUIT_BREAKER,
				CircuitBreakerBuilder.buildCircuitBreakerResponse());
		Server server = Grpc.newServerBuilderForPort(PORT, InsecureServerCredentials.create())
				.addService(namingService)
				.build()
				.start();
		LOG.info("Server started, listening on " + PORT);
		Runtime.getRuntime().addShutdownHook(new Thread() {
			@Override
			public void run() {
				// Use stderr here since the logger may have been reset by its JVM shutdown hook.
				System.err.println("*** shutting down gRPC server since JVM is shutting down");
				try {
					NamingServer.stop(server);
				}
				catch (InterruptedException e) {
					e.printStackTrace(System.err);
				}
				System.err.println("*** server shut down");
			}
		});
		blockUntilShutdown(server);
	}

	private static void blockUntilShutdown(Server server) throws InterruptedException {
		if (server != null) {
			server.awaitTermination();
		}
	}

	private static void stop(Server server) throws InterruptedException {
		if (server != null) {
			server.shutdown().awaitTermination(30, TimeUnit.SECONDS);
		}
	}
}
