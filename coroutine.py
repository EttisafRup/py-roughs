def coroutine_rup():
    import time
    time.sleep(4)

    while True:
        find_text = (yield)

        if find_text in "Heda bhai big fan alok dedo":
            print("Mil gya")
        else:
            print("Hello bhai nhi aaya")


rupCORO = coroutine_rup()
next(rupCORO)

rupCORO.send("Heda")
rupCORO.close()
