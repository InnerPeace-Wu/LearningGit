function loss = test(eps)
  loss_p = 0.322890;
  loss = 1;
  lr = 0.005;
  count = 1;
  while ((abs(loss - loss_p) > eps) || (count < 100))
    count += 1;
    loss_p = loss;
    lr += 0.001;
    loss = a4_main(300, .02, lr, 1000);
    printf("lr is : %f, loss is : %f\n", lr, loss);
  end


end
