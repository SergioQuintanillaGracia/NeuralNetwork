#include <iostream>
#include <vector>
#include "network.h"

void printResult(std::vector<double> vec);

int main() {
    // Create the layers of the neural network.
    std::vector<int> layers = {256, 96, 48, 1};

    // Create the NeuralNetwork and GeneticNetworkTrainer objects.
    std::string basePath = "../networks/circles_circumf_16x16/256_96_48_1_mixed";
    std::string pointsPath = "269_270";
    NeuralNetwork* neuralNetwork = new NeuralNetwork(layers, basePath + "/progress/" + pointsPath + ".weights", basePath + "/progress/" + pointsPath + ".bias", false);
    
    GeneticNetworkTrainer trainer(neuralNetwork, basePath, 0, 0.1, 18);

    std::string obj1 = "Circle";
    std::string path1 = "../training/circles16x16_mixed/";
    std::string obj2 = "Circumference";
    std::string path2 = "../training/empty_circles16x16_mixed/";
    trainer.trainBinary(obj1, path1, obj2, path2, 100000, 0.15, &GeneticNetworkTrainer::fitnessPercentageHybrid, true);
    //std::cout << trainer.getFitness(neuralNetwork, path1, path2) << std::endl;
}

void printResult(std::vector<double> vec) {
    std::cout << "Result: ";
    for (double d : vec) {
        std::cout << d << " ";
    }
    std::cout << std::endl;
}