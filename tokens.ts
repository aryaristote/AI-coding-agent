export class coder {
    name: string;
    private musics: string;
    protected age: number;
    public lang: string;

    constructor(name: string, musics: string, age: number, lang: string) {
        this.name = name;
        this.musics = musics;
        this.age = age;
        this.lang = lang;
    }

    public getUser() {
        return `I'm ${this.age} old and I like ${this.musics}`;
    }
}

const coder1 = new coder("John", "Rock", 30, "JavaScript");
// console.log(coder1);
// console.log(coder1.getUser());


class webDev extends coder {
    constructor(name: string, musics: string, age: number, lang: string) {
        super(name, musics, age, lang);
        this.name = name;
        this.age = age;
        this.lang = lang;
    }

    public getwebDev() {
        return `I'm ${this.age} old and I like ${this.musics} and I code in ${this.lang}`;
    }
}

const webDev1 = new webDev("Jane", "Pop", 25, "TypeScript");
console.log(webDev1);