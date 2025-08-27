# 🎮 Jogo da Forca em Python 🪢

## 📝 Descrição
Este é um **jogo da forca** desenvolvido, em Python, onde o jogador deve adivinhar uma palavra escolhida aleatoriamente de uma lista.  
O jogo exibe o progresso das letras, o histórico de tentativas e a forca é desenhada conforme os erros cometidos.  
O terminal utiliza cores para tornar a experiência mais **interativa**.

---

## ✨ Funcionalidades
-  Seleção aleatória de palavras  
-  Mostrar letras descobertas e ocultar as não adivinhadas  
-  Controle de tentativas restantes  
-  Histórico de letras já digitadas  
-  Desenho da forca atualizado a cada erro  
-  Mensagens coloridas no terminal para acertos, erros e status do jogo  

---

## 🎮 Como jogar
1. Execute o script `forca.py`  
2. O programa exibirá a palavra com `_` representando letras não descobertas  
3. Digite **uma letra por vez**  
4. O programa verifica se a letra está na palavra:  
   - ✅ Se sim, revela a letra nos lugares corretos  
   - ❌ Se não, diminui uma tentativa e atualiza o desenho da forca  
5. O jogo termina quando:  
   - 🏆 O jogador adivinha todas as letras → **vitória**  
   - 💀 O jogador esgota todas as tentativas → **derrota**, revelando a palavra secreta  
