import json

j = '{"one" : "1", "two" : "2", "three" : "3"}'
loaded_json = json.loads(j,encoding=None)
for x in loaded_json:
    print (x, loaded_json[x], '\n')

#data ='{"success":true,"data":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50SWQiOiI1YTU0Y2QwZGNmNmVhZTViZTdkOTdlN2IiLCJjb21wYW55SWQiOiI1YTU0Y2M1MGNmNmVhZTViZTdkOTdlNTciLCJ1c2VybmFtZSI6ImNvbXBhbnkxX29wZXJhdG9yIiwicm9sZSI6Im9wZXJhdG9yIiwiY2xpZW50VHlwZSI6InBsYW50IiwicGxhbnRJZCI6IjVhNDExY2JmNTkwMWY3NGJjY2UyOTczMSIsImlhdCI6MTUzMzM0MDQ1NSwiZXhwIjoxNTMzNDI2ODU1fQ.i58Z-LS7nw9pf_qG5en9bU_EkdsF1qQJmJ6bdrTF62M"}'
#js = json.load(data)
#print (js)