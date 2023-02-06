import datetime

print()
print()

x = datetime.datetime.now()
y = datetime.datetime(2022,1,28)

print(f"TODAY IS: {y}")

begin = datetime.datetime(1994,7,11)
end = datetime.datetime(2069,7,11)

age = y - begin
total = end - begin

print(f"YOUR JOURNEY IS {(age/total)*100} %  COMPLETE")

print()
print()
