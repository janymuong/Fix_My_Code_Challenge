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
$ curl -XGET http://0.0.0.0:5000/api/v1/status
{
  "error": "Not found"
}
$
```

- Woeking API:
```bash
# 
```
