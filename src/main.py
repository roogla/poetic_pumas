from Vector2D import Vector2D
from Physics import RigitBody


def main():
    newbody = RigitBody(10, 10)
    gravity = Vector2D(0, -2)
    print(newbody)
    newbody.apply_force(gravity)
    newbody.update()
    print(newbody)


if __name__ == '__main__':
    main()
