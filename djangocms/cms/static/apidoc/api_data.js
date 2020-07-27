define({ "api": [
  {
    "type": "post",
    "url": "/user/register/",
    "title": "01 注册",
    "group": "10",
    "name": "user_register",
    "version": "1.0.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "phone",
            "description": "<p>账号，就是手机号</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "password",
            "description": "<p>密码</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "code",
            "description": "<p>六位数字验证码,注意是字符串</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "获取数据",
          "content": "{\n    \"phone\": \"15935725812\",\n    \"password\": \"qwer1234\",\n    \"code\": \"666666\"\n}",
          "type": "Array"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "int",
            "optional": false,
            "field": "user_id",
            "description": "<p>用户id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "返回数据",
          "content": "返回值类型: JSON\n{\n  \"message\": \"\",\n  \"data\": {\n    \"user_id\": 111\n  },\n  \"response\": \"ok\",\n  \"error\": \"\"\n}",
          "type": "Array"
        }
      ]
    },
    "filename": "../cms/apps/user/views.py",
    "groupTitle": "用户"
  }
] });
