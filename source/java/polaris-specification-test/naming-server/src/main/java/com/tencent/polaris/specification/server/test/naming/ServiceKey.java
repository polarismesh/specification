/*
 * Tencent is pleased to support the open source community by making Polaris available.
 *
 * Copyright (C) 2021 Tencent. All rights reserved.
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

import java.util.Objects;

public class ServiceKey {

	private final String namespace;

	private final String service;

	public ServiceKey(String namespace, String service) {
		this.namespace = namespace;
		this.service = service;
	}

	public String getNamespace() {
		return namespace;
	}

	public String getService() {
		return service;
	}

	@Override
	public String toString() {
		return "ServiceKey{" +
				"namespace='" + namespace + '\'' +
				", service='" + service + '\'' +
				'}';
	}

	@Override
	public boolean equals(Object o) {
		if (this == o) return true;
		if (o == null || getClass() != o.getClass()) return false;
		ServiceKey that = (ServiceKey) o;
		return Objects.equals(namespace, that.namespace) && Objects.equals(service, that.service);
	}

	@Override
	public int hashCode() {
		return Objects.hash(namespace, service);
	}
}
