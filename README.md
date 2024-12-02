# Credential Helper

AWS環境にアクセスするには、AWS SSOで認証し各プロダクトのメンテナンスロールにスイッチロールする必要があります。  
ローカルPC上のPythonから操作したい場合には、AWS CLIにてプロファイルで管理させたとしても面倒です。  

Credential Helperは、AWS SSOを通した認証と各プロダクトのメンテナンス用ロールの一時認証情報の取得を助けます。  
Pythonを使って複数環境を跨った操作を自動化したい場合などにお使い下さい。

例えば、Lambdaのタグに設定したバージョン情報を全環境分取得して表示したい場合は、以下のように書くことができます。

実行時には、必要に応じてブラウザにて認証確認を求められますので、許可して下さい。  
AWS SSOの認証tokenはファイルにキャッシュし、有効期間内であれば再利用します。  
また、キャッシュはホームディレクトリに固定名称のファイルとして保存し、Credential Helperを使った複数のプログラムで共有して再利用します。

## How to use

### Credentialsの構造
AccountIDを入れてます
```python
{
    'AccessKeyId': 'XXXXXXXXXXXXX',
    'SecretAccessKey': 'YYYYYYYYY',
    'SessionToken': 'ZZZZZZZZZZ',
    'Expiration': 有効期限,
    'AccountID': 'アカウントID'
}
```

## How to install
