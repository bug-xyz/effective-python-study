define({
  "name": "djangocmsAPI",
  "version": "2.0.0",
  "description": "django学习demo",
  "title": "djangocmsAPI",
  "url": "http://192.168.13.96:9000",
  "header": {
    "title": "djangocmsAPI",
    "content": "<h3>概述:</h3>\n<p><strong>请求说明:</strong></p>\n<ul>\n<li>本API全部请求采用http POST 请求</li>\n<li>请求、响应全部json格式数据</li>\n<li>除登录接口外，全部接口需要header加参数 sessionid:登录后服务端返回</li>\n</ul>\n<p><strong>异常状态:</strong></p>\n<ul>\n<li>\n<p>一般状态\n<code>{&quot;message&quot;: &quot;数据获取失败，请重试&quot;, &quot;error&quot;: &quot;&quot;, &quot;data&quot;: &quot;&quot;, &quot;response&quot;: &quot;fail&quot;, &quot;next&quot;: &quot;&quot;}</code></p>\n</li>\n<li>\n<p>特殊状态</p>\n<p><code>{&quot;message&quot;: &quot;更新失败&quot;, &quot;error&quot;: &quot;&quot;, &quot;data&quot;: {&quot;error&quot;: 1}, &quot;response&quot;: &quot;fail&quot;, &quot;next&quot;: &quot;&quot;}</code></p>\n<table>\n<thead>\n<tr>\n<th>error编码值</th>\n<th>用处</th>\n<th>含义</th>\n</tr>\n</thead>\n<tbody>\n<tr>\n<td>1</td>\n<td>所有api</td>\n<td>软件版本需要更新</td>\n</tr>\n<tr>\n<td>2</td>\n<td>非登录注册设置api</td>\n<td>会话过期，需要重新回到手机检测</td>\n</tr>\n<tr>\n<td>3</td>\n<td>非登录注册设置api</td>\n<td>进入用户设置页面<br>user_type:1正式账号，0体验账号；<br/>set_status:1正式账号未配置，2正式账号已配置未激活，3正式账号已失效</td>\n</tr>\n<tr>\n<td>4</td>\n<td>非登录注册设置api</td>\n<td>帐号被禁用，请联系管理员</td>\n</tr>\n<tr>\n<td>6</td>\n<td>体验账号登录api，需弹窗</td>\n<td>体验账号正在使用中</td>\n</tr>\n<tr>\n<td>7</td>\n<td>正式账号登录api，需弹窗</td>\n<td>输入的密码连续错误三次，是否重置密码</td>\n</tr>\n<tr>\n<td>8</td>\n<td>体验账号登录api，需弹窗</td>\n<td>该账号当日已被禁用，次日恢复使用</td>\n</tr>\n<tr>\n<td>9</td>\n<td>获取手机验证码api</td>\n<td>验证码获取次数已达当日上限</td>\n</tr>\n</tbody>\n</table>\n</li>\n</ul>\n<p><strong>成功状态:</strong>\n<code>{&quot;message&quot;: &quot;数据获取失败，请重试&quot;, &quot;error&quot;: &quot;&quot;, &quot;data&quot;: {}, &quot;response&quot;: &quot;fail&quot;, &quot;next&quot;: &quot;&quot;}</code></p>\n<p><strong>注意事项:</strong></p>\n<ul>\n<li>SessionID为客户端与服务器用户认证的SessionID,除登录接口、检测更新接口外，其他接口每次请求的时候必传该值</li>\n<li>API请求方式为GET、POST请求<br><br></li>\n</ul>\n"
  },
  "template": {
    "forceLanguage": "zh_cn",
    "withCompare": false,
    "withGenerator": true
  },
  "sampleUrl": false,
  "defaultVersion": "0.0.0",
  "apidoc": "0.3.0",
  "generator": {
    "name": "apidoc",
    "time": "2020-07-30T08:38:53.829Z",
    "url": "http://apidocjs.com",
    "version": "0.17.7"
  }
});
