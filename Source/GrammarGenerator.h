#ifndef _GRAMMAR_GENERATOR_H
#define _GRAMMAR_GENERATOR_H

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

/*
    The grammar generator parses a csv file to understand the language implementation.
    Impletations will be done using a standard dictionary to describe how functions,
    internal memory structures, and other operations behave
*/

class GrammarGenerator {

    public:

        GrammarGenerator();
        ~GrammarGenerator();

        void readFile(std::string langTemplate);

    private: 
    
        // ------ PARAMETERS ------------

};

#endif /* _GRAMMAR_GENERATOR_H */