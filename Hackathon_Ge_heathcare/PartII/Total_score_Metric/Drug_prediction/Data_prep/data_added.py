import pandas
df=pandas.read_csv("../data.csv")
print df.head()
def y(x):
    y=0.5*x+0.1
    return y
def z(x):
    z=-0.2*x+0.05
    return z

df["Visit2"][0:520]=y(df["Visit1"][0:520])+random.random()*0.01
df["Visit2"][520:]=z(df["Visit1"][520:])+random.random()*0.01

df["Visit3"][0:520]=y(df["Visit2"][0:520])+random.random()*0.01
df["Visit3"][520:]=z(df["Visit2"][520:])+random.random()*0.01

df["Visit4"][0:520]=y(df["Visit3"][0:520])+random.random()*0.01
df["Visit4"][520:]=z(df["Visit3"][520:])+random.random()*0.01

df["Visit5"][0:520]=y(df["Visit4"][0:520])+random.random()*0.01
df["Visit5"][520:]=z(df["Visit4"][520:])+random.random()*0.01

df["Visit6"][0:520]=y(df["Visit5"][0:520])+random.random()*0.01
df["Visit6"][520:]=z(df["Visit5"][520:])+random.random()*0.01

df["Visit7"][0:520]=y(df["Visit6"][0:520])+random.random()*0.01
df["Visit7"][520:]=z(df["Visit6"][520:])+random.random()*0.01

df["Visit8"][0:520]=y(df["Visit7"][0:520])+random.random()*0.01
df["Visit8"][520:]=z(df["Visit7"][520:])+random.random()*0.01

df["Visit9"][0:520]=y(df["Visit8"][0:520])+random.random()*0.01
df["Visit9"][520:]=z(df["Visit8"][520:])+random.random()*0.01

df["Visit10"][0:520]=y(df["Visit9"][0:520])+random.random()*0.01
df["Visit10"][520:]=z(df["Visit9"][520:])+random.random()*0.01

df["Visit11"][0:520]=y(df["Visit10"][0:520])+random.random()*0.01
df["Visit11"][520:]=z(df["Visit10"][520:])+random.random()*0.01

df["Visit12"][0:520]=y(df["Visit11"][0:520])+random.random()*0.01
df["Visit12"][520:]=z(df["Visit11"][520:])+random.random()*0.01

df.to_csv("data.csv")

