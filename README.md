# TCC
Trabalho de Conclusão de Curso - Sistemas da Informação 2019

## Análise da importância de características na detecção de Malwares para sistemas Android

À medida que os dispositivos móveis baseados em Android se tornam cada vez mais populares, cresce o número de aplicativos que lidam com dados financeiros e pessoais. Esse fato mostrou ao mercado do crime cibernético que o ecossistema Android é um alvo muito atraente e rentável. Por esse motivo, os fraudadores estão produzindo mais aplicativos maliciosos compatíveis com essa plataforma. Hoje, analisar Malwares de forma individual é inviável pelo gasto de tempo com essa tarefa e pela grande quantidade de aplicativos lançados diariamente no mercado digital. Assim, torna-se indispensável fazer o uso de detectores automáticos de “Programas Maliciosos”. Neste trabalho foi feita uma análise de detectores de Malwares baseados em aprendizagem de máquina com foco em Android. Agrupados 5079 aplicativos maliciosos coletados de três bases de Malwares, foram extraídas diferentes features dos aplicativos coletados e utilizadas como insumo para criação de diferentes modelos de aprendizagem de máquina para detecção. A partir desses testes foi constatado que o uso de “intents” dos aplicativos com Random Forest conseguem produzir bons resultados na detecção de Malware em Android. 

### Bases de Dados Utilizadas

* [AndroZoo](https://androzoo.uni.lu/) - Android Malware collection
* [VirusShare](https://virusshare.com/) - Repository of Malware samples
* [Github_Malware](https://github.com/ashishb/android-malware) - Cool collection of Android Malware
* [UNB_Malware](https://www.unb.ca/cic/datasets/android-adware.html) - Android Adware and General Malware Dataset (Benign)
