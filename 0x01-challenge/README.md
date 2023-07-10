# Fix-my-code-1

> solutions to the random bugs in files.

Compare the files in here with the original regular files in the directory.

`Diff`:  

This is a sample of what has been fixed.
- Buggy API:
```bash
$ python -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

```bash
$ curl -XGET http://0.0.0.0:5000/api/v1/status
{
  "error": "Not found"
}
$
```

- Working API:
```bash
root@HP:/0x01-challenge/status_server# python3 -m api.v1.app
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.230.179:5000
Press CTRL+C to quit
127.0.0.1 - - [10/Jul/2023 22:07:41] "GET /api/v1/status HTTP/1.1" 200 -
```

```bash
mu-o@HP:~$ curl -XGET http://0.0.0.0:5000/api/v1/status
{"status":"OK"}
```
