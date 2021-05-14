x, y, w, h =input().split()

x = int(x)
y = int(y)
w = int(w)
h = int(h)
X = w - x
Y = h - y

print(min(x, y, X, Y))
