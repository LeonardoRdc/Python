''' Esse exercício deve ser feito pelos alunos em duplas, durante nossas aulas. Depois de feitas as modificações no código os alunos devem submeter o código ao github e submeter o link aqui.

Para um dos dois códigos disponíveis (o código da aula prática 02 ou da aula prática 03), faça o seguinte:

1. Crie um dataset da sua escolha, descrevendo o que são as entradas e a saída.

2. Em seguida, treine duas instâncias do seu modelo (sua rede neural): uma usando função de ativação sigmoid, e outra usando função de ativação relu. 

3. Submeta seu código ao github, e envie links por aqui (um link para cada modelo), de forma que sua tarefa seja corrigida. '''

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)


def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

def relu_derivative(x):
    return np.where(x > 0, 1, 0)


iris = load_iris()
X = iris.data[:100, :]  
y = iris.target[:100].reshape(-1, 1)


scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


def train_nn(activation, activation_derivative, epochs=5000, learning_rate=0.01):
    np.random.seed(42)
    input_size = X_train.shape[1]
    hidden_size = 5
    output_size = 1

    
    W1 = np.random.randn(input_size, hidden_size)
    b1 = np.random.randn(hidden_size)
    W2 = np.random.randn(hidden_size, output_size)
    b2 = np.random.randn(output_size)

    errors = []

    for epoch in range(epochs):
        
        z1 = np.dot(X_train, W1) + b1
        a1 = activation(z1)
        z2 = np.dot(a1, W2) + b2
        a2 = sigmoid(z2)  

        
        error = y_train - a2
        errors.append(np.mean(np.square(error)))

        
        d_a2 = -2 * error / len(X_train)
        d_z2 = d_a2 * sigmoid_derivative(z2)
        d_W2 = np.dot(a1.T, d_z2)
        d_b2 = np.sum(d_z2, axis=0)

        d_a1 = np.dot(d_z2, W2.T)
        d_z1 = d_a1 * activation_derivative(z1)
        d_W1 = np.dot(X_train.T, d_z1)
        d_b1 = np.sum(d_z1, axis=0)

        
        W2 -= learning_rate * d_W2
        b2 -= learning_rate * d_b2
        W1 -= learning_rate * d_W1
        b1 -= learning_rate * d_b1

    
    plt.plot(range(epochs), errors)
    plt.title(f"Gráfico ({activation.__name__})")
    plt.xlabel("Épocas")
    plt.ylabel("Erro")
    plt.show()

    
    z1 = np.dot(X_test, W1) + b1
    a1 = activation(z1)
    z2 = np.dot(a1, W2) + b2
    a2 = sigmoid(z2)

    predictions = (a2 > 0.5).astype(int)
    accuracy = np.mean(predictions == y_test)
    print(f"Acurácia no teste ({activation.__name__}): {accuracy:.2f}")


train_nn(sigmoid, sigmoid_derivative)
train_nn(relu, relu_derivative)
