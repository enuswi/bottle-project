 <!DOCTYPE html>
    <html>
        <body>
            <div class="mui-container">
                <div class="mui-panel">
                    <h1>ユーザー詳細</h1>
                    <link rel="stylesheet" type="text/css" href="/static/css/mui.css">
                    <link rel="stylesheet" type="text/css" href="/static/css/mui.min.css">

                    <form name="update_user" class="mui-form" method="POST" action="/updateUser/{{user_info[0]}}">
                        <div class="mui-textfield">
                            name: <input type="text" name="user_name" value="{{user_info[1]}}" required><br />
                        </div>
                        <input type="submit" class="mui-btn mui-btn--raised" value="変更">
                    </form>

                    <form name="delete_user" method="POST" action="/deleteUser/{{user_info[0]}}">
                        <input type="submit" class="mui-btn mui-btn--primary mui-btn--raised" value="削除">
                    </form>
                </div>
            </div>
        </body>
 </html>