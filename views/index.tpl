    <!DOCTYPE html>
    <html>
        <body>
            <div class="mui-container">
                <div class="mui-panel">
                    <h1>ユーザー一覧</h1>
                    <link rel="stylesheet" type="text/css" href="/static/css/mui.css">
                    <link rel="stylesheet" type="text/css" href="/static/css/mui.min.css">
                    <!-- 新規ユーザー登録 -->
                    <form name="create_user" class="mui-form" method="POST" action="/createUser">
                        <div class="mui-textfield">
                            name: <input type="text" name="user_name" required placeholder="tanaka taro"><br />
                            email: <input type="text" name="user_email" required placeholder="tanaka@tanaka.com"><br />
                            password: <input type="password" name="user_password" required><br />
                        </div>
                        <input type="submit" class="mui-btn mui-btn--raised" value="登録">

                    </form><br />
                    <table class="mui-table mui-table--bordered">
                        <tr>
                            <td><b>id</b></td>
                            <td><b>name</b></td>
                            <td><b>email</b></td>
                            <td><b>update</b></td>
                        </tr>
                            % for user in user_list:
                        <tr>
                            <td>{{user[0]}}</td>
                            <td>{{user[1]}}</td>
                            <td>{{user[2]}}</td>
                            <td>
                                <form name="update_user" method="POST" action="/showUser/{{user[0]}}">
                                    <input type="submit" class="mui-btn mui-btn--primary mui-btn--raised" value="更新">
                                </form>
                                <form name="delete_user" method="POST" action="/deleteUser/{{user[0]}}">
                                    <input type="submit" class="mui-btn mui-btn--primary mui-btn--raised" value="削除">
                                </form>
                            </td>
                        </tr>
                            % end
                    </table>
                </div>
            </div>
        </body>
    </html>