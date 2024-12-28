#include "GrammarGenerator.h"

GrammarGenerator::GrammarGenerator(){}

GrammarGenerator::~GrammarGenerator(){}

void GrammarGenerator::readFile(std::string langTemplate)
{
    std::ifstream file(langTemplate);
    std::string line;

    while (std::getline(file, line)) {
        std::stringstream ss(line);
        std::string cell;
        std::vector<std::string> row;

        while (std::getline(ss, cell, '\t')) { 
            row.push_back(cell);
        }

        for (const auto &value : row) {
            std::cout << value << " ";
        }
        
        std::cout << std::endl;
    }

    file.close();
}