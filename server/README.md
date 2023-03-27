# BSSHOP soutěž v programování 2023

## Server pro provoz hry

Tato složka obsahuje zkompilovaný server se hrou, který žádá servery hadů o jejich směr pohybu v každé iteraci.

Server lze spustit souborem `run.cmd`.

### Nastavení

V souboru `BsSnake.Server\appsettings.json` je třeba mít sekci
```json
"Kestrel": {
	"Endpoints": {
		"Http": {
			"Url": "http://127.0.0.1:6100"
		}
    }
}
```

Na této adrese a portu běží webové rozhraní se hrou.

V souboru `BsSnake.Server\snakes.json` je seznam hadů, které server očekává (nemusejí nutně běžet). Pomocí webového rozhraní vyberete, kteří hadi se budou účastnit konkrétní hry.

V souboru `BsSnake.Server\games.json` je seznam konfigurací hry (parametry měnící obtížnost a další). Pomocí webového rozhraní vyberete, kterou konkrétní konfiguraci chcete spustit.
