from nada_dsl import *

def nada_main():
    deadalive = Party(name="Dead/Alive")

    my_int1 = SecretInteger(Input(name="my_int1", party=deadalive))
    my_int2 = SecretInteger(Input(name="my_int2", party=deadalive))

    int1 = my_int1 % 6  # Modulo operation on my_int1
    int2 = my_int2 % 6  # Modulo operation on my_int2

    # Check the results of the modulo operation
    if int1 == 0:
        new_int = SecretInteger(1)
    elif int2 == 0:
        new_int = SecretInteger(2)
    else:
        new_int = SecretInteger(0)

    # Return the output to the party
    return [Output(new_int, "my_output", deadalive)]
