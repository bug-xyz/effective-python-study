define({ "api": [
  {
    "type": "post",
    "url": "/user/change_pwd/",
    "title": "04 重置密码",
    "group": "10",
    "name": "user_change_pwd",
    "version": "1.0.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "username",
            "description": "<p>手机号</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "code",
            "description": "<p>手机验证码，注意是字符串格式</p>"
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
            "field": "confirm",
            "description": "<p>密码确认</p>"
          }
        ]
      }
    },
    "examples": [
      {
        "title": "获取数据",
        "content": "获取值类型:JSON\n{\n    \"usernam\": \"11111111112\",\n    \"code\": \"666666\",\n    \"password\": \"1234qwer\"\n    \"confirm\": \"1234qwer\"\n}",
        "type": "Array"
      }
    ],
    "success": {
      "examples": [
        {
          "title": "返回数据",
          "content": "返回值类型: JSON\n{\n   \"message\": \"\",\n   \"data\": {},\n   \"response\": \"ok\",\n   \"error\": \"\"\n}",
          "type": "Array"
        }
      ]
    },
    "filename": "../cms/apps/user/views.py",
    "groupTitle": "用户"
  },
  {
    "type": "post",
    "url": "/user/login/",
    "title": "02 登陆",
    "group": "10",
    "name": "user_login",
    "version": "1.0.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "username",
            "description": "<p>账号，就是手机号</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "password",
            "description": "<p>密码</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "获取数据",
          "content": "{\n    \"username\": \"15935725812\",\n    \"password\": \"qwer1234\"\n}",
          "type": "Array"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "string",
            "optional": false,
            "field": "username",
            "description": "<p>账号</p>"
          },
          {
            "group": "Success 200",
            "type": "int",
            "optional": false,
            "field": "user_id",
            "description": "<p>用户id</p>"
          },
          {
            "group": "Success 200",
            "type": "string",
            "optional": false,
            "field": "name",
            "description": "<p>用户真实姓名</p>"
          },
          {
            "group": "Success 200",
            "type": "int",
            "optional": false,
            "field": "gender",
            "description": "<p>性别，0未设置，1男，2女</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "返回数据",
          "content": "返回值类型: JSON\n{\n    \"response\": \"ok\",\n    \"data\": {\n        \"username\": \"15935725801\",\n        \"user_id\": 1,\n        \"name\": \"\",\n        \"gender\": 1\n    },\n    \"message\": \"\"\n}",
          "type": "Array"
        }
      ]
    },
    "filename": "../cms/apps/user/views.py",
    "groupTitle": "用户"
  },
  {
    "type": "post",
    "url": "/user/logout/",
    "title": "03 退出",
    "group": "10",
    "name": "user_logout",
    "version": "1.0.0",
    "success": {
      "examples": [
        {
          "title": "返回数据",
          "content": "返回值类型: JSON\n{\n  \"message\": \"\",\n  \"data\": \"\",\n  \"response\": \"ok\",\n  \"error\": \"\"\n}",
          "type": "Array"
        }
      ]
    },
    "filename": "../cms/apps/user/views.py",
    "groupTitle": "用户"
  },
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
          }
        ]
      },
      "examples": [
        {
          "title": "获取数据",
          "content": "{\n    \"phone\": \"15935725812\",\n    \"password\": \"qwer1234\",\n}",
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
