// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

    // 24576Ϊ���̵ĵ�ַ 16384-24575 �պ�8K Ϊ��Ļ�ĵ�ַ
    @24575
    D = A

    // R0�洢��Ļ����ַ
    @0
    M = D

    // R1�洢��Ļ��ǰ��ַ
    @SCREEN
    D = A
    @1
    M = D
(LOOP)
    @KBD
    D = M
    @FILL
    D;JGT

    @CLEAR
    0;JMP
(FILL)
    // �ж���Ļ�Ƿ�Ϊ��
    @0
    D = M
    @1
    D = D - M
    @LOOP
    D;JLT

    @1
    // ���浱ǰ��ַ
    D = M
    // ����ǰ��ַ����A
    A = M
    // ����ַ��Ӧ����Ļλ�ñ��
    // ���ʹ�� 1������ɶ������� 0000000000000001
    // -1 ����ɶ������� 1111111111111111
    // �����ʾ����Ļ�ϣ�1 �� 15 λ�ǿհ׵ģ�1λ�Ǻڵ�
    // -1 ����Ļ�ϵ� 16 λȫ�Ǻ�ɫ
    M = -1

    // ��ǰ��ַ+1
    @1
    M = D + 1

    @LOOP
    0;JMP
(CLEAR)
    // �ж���Ļ�Ƿ�Ϊ��
    @SCREEN
    D = A
    @1
    D = D - M
    @LOOP
    D;JGT

    @1
    // ���浱ǰ��ַ
    D = M
    // ����ǰ��ַ����A
    A = M
    // ����ַ��Ӧ����Ļλ�ñ��
    M = 0

    // ��ǰ��ַ-1
    @1
    M = D - 1

    @LOOP
    0;JMP