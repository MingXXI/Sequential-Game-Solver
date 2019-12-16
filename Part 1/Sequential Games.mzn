% Sequential Games


% Given
int: num;                      % Number n ∈ N of games;
int: cap;                      % Pocket Capacity C ∈ N;
set of int: games = 1..num;    % set of game number from 1 to num
array [games] of int: fun;     % Fun value vi ∈ Z for each game i ∈ [n];
int: refill;                   % Refill amount R ∈ N;
int: K;                        % Goal K ∈ N;


% Find
array[1..num] of var int: p;    % sequence of game play
array[1..num] of var int: t;    % number of token in pocket at start of playing each game


% The constraints on t and p are:

  % 1. ∑i∈[n] pivi ≥ K:
  % sum(i, i∈[n], p(i) · v(i)) ≥ K
  constraint sum(i in 1..num) (p[i] * fun[i]) >= K;



  % 2. The number of tokens ti available to play game i is C when we start playing the
  % first game, and for i > 1 is the minimum of C and t[i−1] − p[i−1] + R:
%   constraint (t[1] = cap) /\ ((forall (i in 1..num)
%   ((1 < i /\ i <= num) -> (exists(x in 0..cap) ( (x = (t[i-1] - p[i-1] + refill)) /\
%     ( (x > cap) -> (t[i] = cap) ) /\ ( (x <= cap) -> (t[i] = x) )  )))));
    
     constraint (t[1] = cap) /\ ((forall (i in 1..num)
      ((1 < i /\ i <= num) -> (exists(x in 0..cap+refill) ( (x = (t[i-1] - p[i-1] + refill)) /\
      ( (x > cap) -> (t[i] = cap) ) /\ ( (x <= cap) -> (t[i] = x) )  )))));
    

  % 3. We play each game at least once, and at most t[i] times
  constraint forall (i in 1..num) ((1 <= i /\ i <= num) -> (1 <= p[i] /\ p[i] <= t[i]));


  
%   solve satisfy;
  solve maximize sum(i in 1..num)(p[i] * fun[i]);
  output [show (sum(i in 1..num)(p[i] * fun[i]))];
  output ["\n",show (p)];