def calculo_a_receber(horas,salario,taxa):
    sem_taxa = horas * salario
    receber = sem_taxa * (1 - taxa)
    return receber

