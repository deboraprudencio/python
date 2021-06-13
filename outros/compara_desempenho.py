from time import  time, sleep

class Runtime:
    def __init__(self, method_list, input_list, tester_method):
        self.methods = method_list
        self.inputs = input_list
        self.test = tester_method

        self.runtimes = [[] for i in self.inputs]
        self.faster = [0 for i in self.inputs]
        self.fastest = 0
    
    def __str__(self):
        s = ''
        if self.runtimes.count([]) == len(self.runtimes): s= "Nothing ran"
        else:
            for i in range(len(self.inputs)):
                s += "Input " + str(i)
                s += "\n--------------------------------------------------\n"

                for m in range(len(self.methods)):
                    s += str(self.methods[m].__name__)
                    if self.runtimes[i][m] == None: s+= " ran incorrectly"
                    else: s += " ran in " + str(self.runtimes[i][m]) + " seconds\n"

                s += "\n--------------------------------------------------\n"
                s += str(self.methods[self.faster[i]].__name__) + " was faster"
                s += "\n\n+++++++++++++++++++++++++++++++++++++++++++++++++\n\n"
            
            s += str(self.methods[self.fastest].__name__) + " is the fastest overall"

        return s

    def runtime(self, method_index, input_index):
        if type(self.inputs[input_index]) == list: input = self.inputs[input_index][:]
        else: input = self.inputs[input_index]
        
        start_time = time()
        self.methods[method_index](input)
        runtime = time() - start_time

        return runtime
    
    def verify(self, method_index, input_index):
        result = self.methods[method_index](self.inputs[input_index])
        
        return self.test(result)
    
    def run_all(self):
        for i in range(len(self.inputs)):
            for m in range(len(self.methods)):
                if self.verify(m, i):
                    self.runtimes[i].append(self.runtime(m, i))
                    if self.runtimes[i][m] < self.runtimes[i][self.faster[i]]:
                        self.faster[i] = m
                else: self.runtimes[i].append(None)
        
        most_faster_runs = 0
        for method_index in self.faster:
            faster_runs_count = self.faster.count(method_index)
            if faster_runs_count > most_faster_runs:
                self.fastest = method_index
                most_faster_runs = faster_runs_count

        return self

if __name__ == "__main__":
    def lento(n):
        sleep(2)
        return True
    
    def rapido(n):
        sleep(1)
        return True
    
    def variavel(n):
        sleep(n)
        return True
    
    def errado(n):
        return False
    
    def tester_method(result):
        return result
    
    method_list = [lento, rapido, variavel, errado]
    input_list = [0, 1.5, 2]
    
    print(Runtime(method_list, input_list, tester_method).run_all())

    # Erros a corrigir:
    # faster[i] = Nonetype --> quando isso acontece?
    # Transformar método verificador em opcional (fazer que quando ele é igual ao valor de inicialização, não faz a verificação)
