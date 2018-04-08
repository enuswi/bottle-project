<!DOCTYPE html>
<html>
    <body>
    <h1>ユーザー一覧</h1>
    <!-- 新規ユーザー登録 -->
    <form name="create_user" method="POST" action="/createUser">
        name: <input type="text" name="user_name" required><br />
        email: <input type="text" name="user_email" required><br />
        password: <input type="password" name="user_password" required><br />
        <input type="submit" value="登録">

    </form><br />
    <table>
        <tr>
            <td>id</td>
            <td>name</td>
            <td>email</td>
        </tr>
            % for user in user_list:
        <tr>
            <td>{{user[0]}}</td>
            <td>{{user[1]}}</td>
            <td>{{user[2]}}</td>
            <td>
                <form name="update_user" method="POST" action="/showUser/{{user[0]}}">
                    <input type="submit" value="更新">
                </form>
            </td>
            <td>
                <form name="delete_user" method="POST" action="/deleteUser/{{user[0]}}">
                    <input type="submit" value="削除">
                </form>
            </td>
        </tr>
            % end
    </table>
    </body>
</html>