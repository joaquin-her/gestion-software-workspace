#!/bin/bash

# Setup Workspace Script (Linux/Mac)
# Este script crea enlaces simbólicos desde .agent a las carpetas que los IDEs reconocen.

SOURCE_DIR=".agent"
TARGETS=(".vscode" ".cursor" ".windsurf")

if [ ! -d "$SOURCE_DIR" ]; then
    echo -e "\e[31mError: La carpeta fuente '$SOURCE_DIR' no existe.\e[0m"
    exit 1
fi

for target in "${TARGETS[@]}"; do
    if [ -e "$target" ]; then
        echo -e "\e[33mLa carpeta '$target' ya existe. Omitiendo...\e[0m"
    else
        echo -e "\e[36mCreando enlace para $target...\e[0m"
        ln -s "$SOURCE_DIR" "$target"
        if [ $? -eq 0 ]; then
            echo -e "\e[32mExito: $target vinculado a $SOURCE_DIR\e[0m"
        else
            echo -e "\e[31mError al crear el enlace para $target\e[0m"
        fi
    fi
done

echo -e "\nConfiguracion completada. Ahora puedes usar el IDE de tu preferencia."
