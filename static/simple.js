function fetch_example(){
       let fetchRes = fetch("http://127.0.0.1:8000/index/simple_fetch");

        fetchRes.then(res =>
            res.json()).then(d => {
                console.log(d)
            })
}