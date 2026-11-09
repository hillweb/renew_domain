# renew_domain
digitalplat域名自动续费;dnshe域名自动续费;digitalplat API;dnshe API;

## digitalplat API
> https://dashboard.digitalplat.org/dashboard/api/docs
>
> 永久
>
> 120天续费
> 
- 获取域名列表
```bash
# bash
curl https://domain-api.digitalplat.org/api/v1/domains \
  -H "Authorization: Bearer dp_live_xxxxxxxxxxxxxxxxx"
```
```python
# python
import requests

response = requests.get(
    "https://domain-api.digitalplat.org/api/v1/domains",
    headers={"Authorization": "Bearer dp_live_xxxxxxxxxxxxxxxxx"},
    timeout=30,
)

result = response.json()
print(result["data"])
```
```js
//javascript
const response = await fetch("https://domain-api.digitalplat.org/api/v1/domains", {
  headers: {
    Authorization: "Bearer dp_live_xxxxxxxxxxxxxxxxx"
  }
});

const result = await response.json();
console.log(result.data);
```

- 续费已注册域名

```bash
#bash
curl https://domain-api.digitalplat.org/api/v1/domains/example.us.kg/renew \
  -X POST \
  -H "Authorization: Bearer dp_live_xxxxxxxxxxxxxxxxx" \
  -H "Content-Type: application/json" \
  -d '{ "years": 1, "payment_method": "sandbox" }'
```
```python
#python
import requests

response = requests.request(
    "POST",
    "https://domain-api.digitalplat.org/api/v1/domains/example.us.kg/renew",
    headers={"Authorization": "Bearer dp_live_xxxxxxxxxxxxxxxxx"},
    json={ "years": 1, "payment_method": "sandbox" },
    timeout=30,
)

print(response.json())
```
```js
//javascript
const response = await fetch("https://domain-api.digitalplat.org/api/v1/domains/example.us.kg/renew", {
  method: "POST",
  headers: {
    Authorization: "Bearer dp_live_xxxxxxxxxxxxxxxxx",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ "years": 1, "payment_method": "sandbox" })
});

console.log(await response.json());
```
