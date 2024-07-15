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

package com.tencent.polaris.specification.server.test.builder;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.stream.Collectors;

import com.google.protobuf.InvalidProtocolBufferException;
import com.google.protobuf.StringValue;
import com.google.protobuf.UInt32Value;
import com.google.protobuf.util.JsonFormat;
import com.tencent.polaris.specification.api.v1.fault.tolerance.CircuitBreakerProto;
import com.tencent.polaris.specification.api.v1.model.CodeProto;
import com.tencent.polaris.specification.api.v1.service.manage.ResponseProto;
import com.tencent.polaris.specification.api.v1.service.manage.ServiceProto;

public class CircuitBreakerBuilder {

	public static ResponseProto.DiscoverResponse buildCircuitBreakerResponse() throws InvalidProtocolBufferException {
		CircuitBreakerProto.CircuitBreaker.Builder circuitBreakerBuilder =
				CircuitBreakerProto.CircuitBreaker.newBuilder();
		circuitBreakerBuilder.addRules(loadRule("circuitBreakerRule1.json"));
		circuitBreakerBuilder.addRules(loadRule("circuitBreakerRule2.json"));
		ResponseProto.DiscoverResponse.Builder builder = ResponseProto.DiscoverResponse.newBuilder();
		builder.setCode(UInt32Value.newBuilder().setValue(CodeProto.Code.ExecuteSuccess_VALUE).build());
		builder.setInfo(StringValue.newBuilder().setValue("ok").build());
		builder.setService(ServiceProto.Service.newBuilder().setNamespace(
				StringValue.newBuilder().setValue("Test").build()).setName(
				StringValue.newBuilder().setValue("TestSvc").build()).build());
		builder.setCircuitBreaker(circuitBreakerBuilder.build());
		builder.setType(ResponseProto.DiscoverResponse.DiscoverResponseType.CIRCUIT_BREAKER);
		return builder.build();
	}

	public static CircuitBreakerProto.CircuitBreakerRule loadRule(String fileName) throws InvalidProtocolBufferException {
		CircuitBreakerProto.CircuitBreakerRule.Builder circuitBreakerRuleBuilder = CircuitBreakerProto.CircuitBreakerRule
				.newBuilder();
		InputStream inputStream = CircuitBreakerBuilder.class.getClassLoader()
				.getResourceAsStream("circuitBreakerRule1.json");
		String json = new BufferedReader(new InputStreamReader(inputStream, StandardCharsets.UTF_8)).lines()
				.collect(Collectors.joining(""));
		JsonFormat.parser().ignoringUnknownFields().merge(json, circuitBreakerRuleBuilder);
		return circuitBreakerRuleBuilder.build();
	}

}
