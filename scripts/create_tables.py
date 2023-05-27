from common.base import Base, engine

# from common.tables import PprRawAll, PprCleanAll


def main():
    print("[Create Tables] Start")
    Base.metadata.create_all(engine)
    print("Tables Created")
    print("[Create Tables] End")


# if __name__ == "__main__":
#     Base.metadata.create_all(engine)
#     print("Tables Created")
