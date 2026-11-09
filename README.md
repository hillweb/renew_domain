# renew_domain
digitalplat域名自动续费;dnshe域名自动续费;digitalplat API;dnshe API;

## 为每个账号创建API KEY
> 单独保存，创建github的 secrets
```json
{
  email:token
}
```

## 根据续费日期自动重置计划任务cron
- 1. 获取并整理所有账号、域名、续费日期
  2. 获取最近需要更新的账号和域名
  3. 获取最近需要更新的日期： 计算提前120天续费的日期，用于更新cron

### Cloudflare
> KV保存账号、域名、续费日期
>
> worker： 获取最近续费日期、最近续费账号和域名；更新KV最新日期
