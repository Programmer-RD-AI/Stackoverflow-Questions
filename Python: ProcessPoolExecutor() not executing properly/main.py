from concurrent.futures import ProcessPoolExecutor


def checktal1(sheet):
    print(f"\nchecktal {sheet}\n")
    return f"Result for {sheet}"


def UpdateMongoDB_Cache(username):
    try:
        print("Updating MongoDB Cache!")
        sheets = ["black", "red"]

        with ProcessPoolExecutor() as executor:
            # Using map to process sheets concurrently
            results = executor.map(checktal1, sheets)

            for sheet, result in zip(sheets, results):
                try:
                    print(f"Processing completed for sheet: {sheet}")

                except Exception as e:
                    print(f"Error processing sheet {sheet}: {e}")

        print("Finished Updating MongoDB Cache!")
    except Exception as e:
        print(f"General error: {e}")


UpdateMongoDB_Cache("test")
