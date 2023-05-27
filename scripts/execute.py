import extract
import create_tables
import transform
import load

if __name__ == "__main__":
    extract.main()
    create_tables.main()
    transform.main()
    load.main()
