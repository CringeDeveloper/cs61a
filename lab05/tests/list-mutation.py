test = {
  'name': 'List Mutation',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # If nothing would be output by Python, type Nothing
          >>> # If the code would error, type Error
          >>> s = [6, 7, 8]
          >>> print(s.append(6))
          None
          >>> s
          [6, 7, 8, 6]
          >>> s.insert(0, 9)
          >>> s
          [9, 6, 7, 8, 6]
          >>> x = s.pop(1)
          >>> s
          [9, 7, 8, 6]
          >>> s.remove(x)
          >>> s
          [9, 7, 8]
          >>> a, b = s, s[:]
          >>> a is s
          True
          >>> b == s
          True
          >>> b is s
          False
          >>> a.pop()
          8
          >>> a + b
          75c70659bcfa1183c7fa83ac12489296
          # locked
          >>> s = [3]
          >>> s.extend([4, 5])
          >>> s
          64a560a48df30fb585341a84030995f3
          # locked
          >>> a
          ebbc4ce3f02bb524db6606ccd8bb5438
          # locked
          >>> s.extend([s.append(9), s.append(10)])
          >>> s
          eb32275e5742fa24d3632207e4fe0e18
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
