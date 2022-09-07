class Perceptron():

    def enseñar_perceptron(self):

        tabla_or = [[0,0,0]
                   ,[0,1,1]
                   ,[1,0,1]
                   ,[1,1,1]]

        tabla_and = [[0,0,0]
                    ,[0,1,0]
                    ,[1,0,0]
                    ,[1,1,1]]

        w0 = 0.9
        w1 = 0.66
        w2 = -0.2