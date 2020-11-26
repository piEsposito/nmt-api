# NMT-API - API for Neural Machine Translation
API for NMT using HuggingFace's Transformers repo and pretrained models.

## Instructions for usage:

 * Clone the repo and `cd` to it:
``` 
git clone https://github.com/piEsposito/nmt-api.git
cd nmt-api

```

 * Set the token on `.env` file and the model name. For default, we are using `Helsinki-NLP/opus-mt-en-roa`, but it should work with any Seq2Seq model for HuggingFace's bucket. 

 * Build the image from Dockerfile:
 
 ```
 docker build . -t nmt-api:v1
 ```
 
 * Run the API server
 
 ```
 docker run -p 8000:8000 nmt-api:v1
 ```

## Consulting the API

To consult the API, you must send a POST request to the URL, using the token. With the default model, the first word must be `>>id<<`, where `id` is the id for the language you want the text to be translated to. 

Here is an example with curl:

```
curl --request POST \
  --url http://localhost:8000/translate \
  --header 'Content-Type: application/json' \
  --header 'TOKEN: token123' \
  --data '{
    "text": ">>por<< The London trio are up for best UK act and best album, as well as getting two nominations in the best song category.\"We got told like this morning '\''Oh I think you'\''re nominated'\''\", said Dappy.\"And I was like '\''Oh yeah, which one?'\'' And now we'\''ve got nominated for four awards. I mean, wow!\"Bandmate Fazer added: \"We thought it'\''s best of us to come down and mingle with everyone and say hello to the cameras. And now we find we'\''ve got four nominations.\"The band have two shots at the best song prize, getting the nod for their Tynchy Stryder collaboration Number One, and single Strong Again.Their album Uncle B will also go up against records by the likes of Beyonce and Kanye West.N-Dubz picked up the best newcomer Mobo in 2007, but female member Tulisa said they wouldn'\''t be too disappointed if they didn'\''t win this time around. "
}'
```

You shoudl get that as an answer:

```
{
  "translation": "O trio de Londres está pronto para o melhor ato do Reino Unido e o melhor álbum, bem como para receber duas nomeações na melhor categoria de música.\"Foi dito como esta manhã 'Oh eu acho que você está nomeado'\", disse Dappy. \"E eu era como 'Oh yeah, qual?' E agora nós temos sido nomeados para quatro prêmios. Quero dizer, wow!\"Bandmate Fazer acrescentou: \"Nós achamos que é melhor de nós baixar e entrar com todos e dizer olá às câmeras. E agora encontramos que temos quatro nomeações.\"A banda tem dois tiros no melhor prêmio de música, recebendo o nod para sua colaboração Tynky Stryder Number One, e Strong Again.Their album Tio B também vai ir contra registros como Beyonce e Kanye West.N-Dubz pegou o melhor novo Mobo em 2007, mas o membro feminino Tulisa disse que eles não seriam muito decepcionados se eles não ganhassem nesta época.",
  "compute_time": 9.075217008590698,
  "words_to_translate_nbr": 149,
  "translated_word_nbr": 146
}
```
