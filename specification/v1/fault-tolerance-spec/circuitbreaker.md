# Circuit breaker（熔断降级）

```yaml
kind: Circuitbreaker
metadata:
  name: ${RuleName}
  service: ${Service Name} # 考虑采用被 Micro Service 关联还是Label Select
  namespace: ${Namespace} 
  interface: ${interface}
spec:
  type: outbound
  destination:
  - namespace:
    service:  #target service name
    interface:
  - namespace:
    service:    
    interface:
  match:
  - key: error
    durdsdds:
    throusdd:
  - key: dsdd
    throusdd:
    dsdasdad:
  - key: slowCall
    slowCallDurationThreshold: ${value} #慢请求时间阈值
    slowCallRateThreshold: ${value} #慢请求熔断比例阈值
  waitDurationInOpenState: ${value} #启动半开状态的时间间隔 
 # isolationLevel: ${SERVICE INSTANCE API} #熔断级别，polaris 默认接口级别，/*实例级别
  minimumNumberOfCalls: ${value} #触发熔断最少请求次数
  maxEjectionPercent: ${value} #最大熔断比例
  faultDetector: ${interface}  #Configured in the provider service：1. 一直探测：无论是否熔断，都一直探测，探测失败就直接熔断，探测成功半开；2. 熔断后探测：实例没有熔断就不探测，实例熔断的话就启动探测，探测成功半开；3. 不探测：永远不执行探测，熔断后等待超时后半开
```

```yaml
kind: Circuitbreaker
metadata:
  name: default
  namespace:
  service:
spec:
  type: outbound
  destination:
  - namespace:
    service:
    interface:
  - namespace:
    service:    
    interface:
  match:
  - key: error
    durdsdds:
    throusdd:
  - key: dsdd
    throusdd:
    dsdasdad:
  halfOpen:
    du
  faultDetector: name
```


