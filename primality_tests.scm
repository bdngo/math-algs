(define (trial-div n)
  (define (td-helper i)
    (cond
      ((> (expt i 2) n) #t)
      ((or (= n 1) (zero? (remainder n i))) #f)
      (else (td-helper (+ i 1)))
    )
  )
  (td-helper 2)
)

(define (map-stream f s)
  (if (null? s)
    nil
    (cons-stream (f (car s)) (map-stream f (cdr-stream s)))
  )
)

(define (search-stream n s)
  (if (or (zero? n) (null? s))
    (car s)
    (search-stream (- n 1) (cdr-stream s))
  )
)

(define lucas-lehmer
  (cons-stream 4 (map-stream (lambda (x) (- (expt x 2) 2)) lucas-lehmer))
)

(define (ll-prime n)
  (if (or (<= n 2) (not (trial-div n)))
    #f
    (let ((luc-leh (search-stream (- n 2) lucas-lehmer)))
      (if (zero? (remainder luc-leh (- (expt 2 n) 1)))
        #t
        #f
      )
    )
  )
)

