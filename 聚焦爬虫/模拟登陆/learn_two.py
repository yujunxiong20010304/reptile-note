'''
https/http协议特性：无状态
cookie用来让服务器记录客户端的相关状态
    1。手动处理：通过抓包工具获取cookie值，将该值封装到headers中（相当于替代了User——Agent），
        但这种方式并不推荐，因为通用性不强，有些网站的cookie还会变化，或限定了时长
    2。自动处理：
        cookie的来源：
            模拟登陆post请求后，由服务器端创建
        session会话对象：
            1。可以进行请求的发送
            2。如果请求过程中产生了cookie则该cookie会被自动存储/携带在该sessiond对象中
        创建一个session对象：session=requests.Ssession()
        使用session对象进行模拟d登陆post请求的发送（cookie就会被存储在session中）
        session对象对个人主页对应的get请求进行发送（携带cookie进行发送）

'''
