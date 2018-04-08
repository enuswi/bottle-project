<!DOCTYPE html>
<html>
    <body>
    <h1>ユーザー名の変更</h1>
    <form name="update_user" method="POST" action="/updateUser/{{userInfo[0]}}">
        name: <input type="text" name="user_name" value="{{userInfo[1]}}" required><br />
        <input type="submit" value="変更">
    </form>
    </body>
</html>