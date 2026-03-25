# Analyse des résultats du Baromètre Science Ouverte de Paris 8

## Le BSO national
Le Baromètre Science Ouverte (BSO) donne à voir l'évolution du nombre de publications dont l'accès est dit « ouvert ». Réalisé la première fois  en 2018, il est mis à jour tous les ans. Par "accès ouvert", le BSO désigne "les publications de recherche mises à disposition librement sur l'internet public" (Le glossaire du BSO [https://barometredelascienceouverte.esr.gouv.fr/a-propos/glossaire](https://barometredelascienceouverte.esr.gouv.fr/a-propos/glossaire)). Prenons deux articles :

1. Stark P., Adil F., Woodward B., Treviño J., Steinhoff C., Gallegos D., 2024, « Real-time Awareness: A Novel Application of Fiber Optics to Optimize Simultaneous Operations of Drilling and Frac », *SPE Hydraulic Fracturing Technology Conference and Exhibition*, p. D031S008R001. https://doi.org/10.2118/217777-MS

2. Firooz S., Reddy B.D., Steinmann P., 2025, « A gradient-enhanced approach for stable finite element approximations of reaction-convection-diffusion problems », *Journal of Theoretical, Computational and Applied Mechanics*, p. 15788. https://doi.org/10.46298/jtcam.15788

Le premier article est dit **"fermé"**, car il est nécessaire d'être abonné à la revue ou d'acheter l'article pour le lire. *A contrario*, le second, que nous avons trouvé sur le Web, est **"ouvert"** : on peut y accèder sans autre condition qu'un accès à Internet.

Selon les observations faites en 2024 par le ministère de l'Enseignement supérieur, de la Recherche et de l'Innovation (MESRI), 105 224 des 160681 publications parues en 2023 et disposant d'un "DOI Crossref" étaient en "accès ouvert", soit un **taux d'ouverture de 66%**. 


## Les baromètres science ouverte locaux

En 2019, l'université de Lorraine reprend la méthode utilisée par le MESRI pour réaliser une déclinaison locale du BSO. Depuis, d'autres établissements d'enseignement supérieur ont voulu avoir leur propre baromètre, conduisant le ministère a élaboré en 2022 une procédure simplifiée. Il "suffit" en effet de télécharger sur le [site du BSO](https://barometredelascienceouverte.esr.gouv.fr/declinaisons/bso-locaux) un fichier CSV contenant les doi des publications de l'établissement, son identifiant ou le nom de sa collection Hal. Ensuite les équipes du BSO extraient depuis leur base de données les publications de l'établissement et leur métadonnées associées. Une fois l'extraction terminée, les résultats peuvent être visualisés directement sur la page du BSO ou depuis une page web de l'établissement.


## Le baromètre de Paris 8

Au printemps 2025, la bibliothèque de Paris 8 a donc décidé de plonger dans Hal et Pubmed pour réaliser son propre baromètre science ouverte local. Les visualisations du baromètre local de Paris 8 sont maintenat disponibles sur le [site web de la bibliothèque](https://www.bu.univ-paris8.fr/services/services-aux-chercheurs/le-barometre-science-ouverte-a-paris-8/). On peut également y accéder via le site du BSO national : Il suffit de se rendre à l'adresse  [https://barometredelascienceouverte.esr.gouv.fr/declinaisons/comment-realiser-bso-local](https://barometredelascienceouverte.esr.gouv.fr/declinaisons/comment-realiser-bso-local) et de rentrer le numéro **199318270** dans la rubrique "Identifiant de l'établissement". Les résultats porte sur la période 2016-2024. Une nouvelle demande a par ailleurs été faite pour intégrer les publications de 2025.

### Processus de collecte

Nous avons repris la procédure proposée par l'université de Lorraine en suivant les "notebooks" disponibles sur Gitlab. Nous avons également construit de nouveaux "notebooks" destiné à automatiser la collecte des données depuis les API de Hal et de Pubmed. Les notebooks sont disponibles sur le dépôt Framagit du SCD de Paris 8 : [collecte_hal](https://framagit.org/scd_paris8/barometre-sciences-ouvertes-universite-paris-8/-/blob/85f8bf985cfe07152056203f48e4dbeeeb638cca/0_script_collect/collecte_hal.ipynb) et [collecte_Pubmed](https://framagit.org/scd_paris8/barometre-sciences-ouvertes-universite-paris-8/-/blob/85f8bf985cfe07152056203f48e4dbeeeb638cca/0_script_collect/collecte_pubmid.ipynb). 

Concrètement, la première étape consiste à définir le périmètre du baromètre local en transmettant à l'équipe du BSO la liste des DOI trouvés sur Pubmed et Hal qui correspondent à des publications dont au moins un des auteurs est affilié à l'université Paris 8. On indique également l'identifiant Hal de l'établissement. Le fichier listant les identifiants (doi ou identifiant Hal) des publications associées à Paris 8 sur la période 2016-2024 contient 9029 lignes. Il est disponible sur [Data Paris 8](https://entrepot.recherche.data.gouv.fr/dataverse/univ-paris8) : 

> Luneau, Aymeric; Arneau, Stéphanie, 2026, "Fichiers envoyés au BSO pour établissement du baromètre science ouverte de Paris 8", [https://doi.org/10.57745/OMEMKY](https://doi.org/10.57745/OMEMKY), Recherche Data Gouv

L'équipe du BSO se charge ensuite de récupérer les métadonnées à partir de Crossref et de Hal. Outre les métadonnées rendues disponibles par les API, l'équipe du BSO a mis en place un ensemble de méthodes pour les enrichir : le statut d'ouverture, la catégorisations disciplinaires, identification de la langue, détecter le pays d'affiliation ([voir la méthodologie du BSO](https://barometredelascienceouverte.esr.gouv.fr/a-propos/methodologie)). Une fois le travail de collecte et de traitement, le BSO nous renvoie les jeu de données en même temps qu'il met en ligne les résultats du baromètre local. Ce jeu de données est constitué de deux fichiers :

En retour, les équipes du BSO renvoient deux fichiers de données : 

* un fichier ".csv" qui ne contient que les données observées lors de l'année en cours. Dans notre cas, le fichier "bso-publications-latest_199318270_enriched.csv" ne contient que le statut des publications observées en 2024.

* un fichier ".jsonl" (json lines) qui contient toutes les données en historique (statut OA pour chaque DOI et à chaque date d'observation).

En effet si un article scientifique n'a qu'une seule **"date de publication"** (date à laquelle il est publié). C’est une donnée qui ne varie pas au cours du temps. Le Baromètre mesure actuellement le taux d’ouverture des publications qui ont été publiées sur la période de 2013 à 2023, un décalage d’un an sur la dernière année de publication étant toujours observé dans le Baromètre national pour prendre en compte les embargos d’ouverture des publications. 

Par contre il peut avoir plusieurs **"date d'observation"**. En effet, depuis le premier baromètre en 2018, l'équipe du BSO produit chaque année une "photographie" de l'état d'ouverture des publications. L’état d’ouverture est ainsi conservé pour chaque année et permet de mesurer l’évolution du taux d’ouverture des publications. Ainsi, si un laboratoire veut comparer le taux d’ouverture de ses publications scientifiques entre deux périodes, il peut visualiser son taux d’ouverture en 2021 par rapport à celui de 2023 par exemple. 

> Claire de Cooman, Laetitia Bracco. Comment valoriser l'ouverture de la production scientifique d'un laboratoire ? Rapport sur l'implémentation d'indicateurs du Baromètre de la Science Ouverte sur deux pages de collection HAL. Université de Lorraine. 2024. ⟨hal-04708155⟩


### Exploiter la richesse des données du Baromètre local

Les analyses réalisées par l'équipe du BSO et rendues visibles par les graphiques publiés sur le site de la bibliothèque se concentrent sur la question de l'ouverture des publications. Elles donnent ainsi à voir l'évolution des voies (ou modalites) d'ouverture au fil des années ou le taux d'ouverture par champs disciplinaires (SHS, sciences biologiques, sciences physiques, etc.). La compréhension des résultats suppose toutefois de plonger dans les données pour saisir les différences entre les modalités d'ouverture des publications ({term}`voie diamant`, {term}`voie dorée`, {term}`voie verte`) ou expliquer pourquoi on a des publications en biologie ou en physique associées à Paris 8 (on verra plus loin que c'est lié à la classification automatique opérée par l'équipe du BSO).

Plonger dans les données permet surtout d'exploiter la richesse des informations qu'elles contiennent. Nous nous sommes en particulier intéressé aux liens tissés par Paris 8 à travers ces publications : les liens entre chercheurs, mais aussi les liens entre les organismes de recherche.

## Reconstruire le réseaux des institutions associées à Paris 8

Parmi les informations présentes dans les données du BSO local, il y en a qui portent sur les affiliations des chercheurs. Cela permet ainsi d'envisager une exploration des relations de Paris 8 avec les autres universités françaises ou étrangères. Toutefois, le travail des donnée a fait apparaître deux cas de figure :

1. les organismes mentionnés sont associés à leur numéro ROR.
2. il n'y a pas de ROR, mais on dispose d'une adresse postale.

Le deuxième cas de figure est plus compliqué puisqu'il suppose d'extraire des informations (nom d'organisme, nom de villes, de Pays) à partir d'information non structurées. Nous nous sommes donc concentrés sur les cas pour lesquels nous disposons du ROR. À cela s'ajoute le fait qu'il n'y a pas toujours d'information concernant les affiliations. Les résultats présentés ci-dessous sont donc partiels et sont à interpréter avec précaution.

### Récupération des informations grâce au ROR

Une fois les rors récupérés, nous avons interrogé l'API du Research Organisation Registry ([https://api.dev.ror.org/organizations](https://api.dev.ror.org/organizations)) puis extrait les données suivantes : le nom de l'organisme, lse noms de la ville, du pays et du continent, ainsi que la latitude et la longitude.




