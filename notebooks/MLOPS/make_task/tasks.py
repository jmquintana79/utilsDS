from invoke import task, Collection
import others

@task
def build(c):
    print("Building!")

@task(build)
def clean(c, all=False):
    if all:
        print("Cleaning all!")
    else:
        print("Cleaning!")
    
@task(help = {"all":"Si se quiere limpiar todo.", 
              "only_one":"Si se quiere limpiar solo uno."})
def clean2(c, all=False, only_one = False):
    if all:
        print("Cleaning all!")
    elif only_one:
        print("Cleaning only-one.")
    else:
        print("Cleaning!")

@task(pre=[build], post=[clean2])
def hello(c, who = ""):
    if who == "":
        msg = "hello world!!"
    else:
        msg = f"hello {who}!!"
    c.run(f"echo '{msg}'")

namespace = Collection(others, build, clean, clean2, hello)