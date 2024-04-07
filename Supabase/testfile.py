from supabase import create_client, Client

url = 'https://kjykbeysqwgibzscbzmr.supabase.co'
with open('creds.txt', 'r') as f:
    content = f.readlines()
    key = content[0]


supabase: Client = create_client(url, key)

response = supabase.table('task').select('category_id(id, name)').execute()
for i in response.data:
    print(i)
