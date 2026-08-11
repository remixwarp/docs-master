class HelloDocs {
  getInfo() {
    return {
      id: 'hellodocs',
      name: 'Hello Docs!',
      // highlight-next-line
      docsURI: 'https://rw-do-cs.pages.dev/development/extensions/docsURI-demo',
      blocks: [
        {
          opcode: 'hello',
          blockType: Scratch.BlockType.REPORTER,
          text: 'Hello!'
        }
      ]
    };
  }

  hello() {
    return Math.random();
  }
}

Scratch.extensions.register(new HelloDocs());
