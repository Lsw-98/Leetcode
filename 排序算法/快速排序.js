function func(arg = 10) {
  console.log(this.p);
  console.log(arg);
}

func.p = 20

const wrapper = func.bind({
  p: 30
})

wrapper()