def bytecode_to_opcode(bytecode):
    opcodes = []
    i = 0

    while i < len(bytecode):
        opcode = bytecode[i:i + 2]  # Extract the opcode bytes
        params = []

        if opcode == '00':
            opcodes.append(['STOP'])
        elif opcode == '01':
            opcodes.append(['ADD'])
        elif opcode == '02':
            opcodes.append(['MUL'])
        elif opcode == '03':
            opcodes.append(['SUB'])
        elif opcode == '04':
            opcodes.append(['DIV'])
        elif opcode == '05':
            opcodes.append(['SDIV'])
        elif opcode == '06':
            opcodes.append(['MOD'])
        elif opcode == '07':
            opcodes.append(['SMOD'])
        elif opcode == '08':
            opcodes.append(['ADDMOD'])
        elif opcode == '09':
            opcodes.append(['MULMOD'])
        elif opcode == '0a':
            opcodes.append(['EXP'])
        elif opcode == '0b':
            opcodes.append(['SIGNEXTEND'])
        elif opcode == '10':
            opcodes.append(['LT'])
        elif opcode == '11':
            opcodes.append(['GT'])
        elif opcode == '12':
            opcodes.append(['SLT'])
        elif opcode == '13':
            opcodes.append(['SGT'])
        elif opcode == '14':
            opcodes.append(['EQ'])
        elif opcode == '15':
            opcodes.append(['ISZERO'])
        elif opcode == '16':
            opcodes.append(['AND'])
        elif opcode == '17':
            opcodes.append(['OR'])
        elif opcode == '18':
            opcodes.append(['XOR'])
        elif opcode == '19':
            opcodes.append(['NOT'])
        elif opcode == '1a':
            opcodes.append(['BYTE'])
        elif opcode == '1b':
            opcodes.append(['SHL'])
        elif opcode == '1c':
            opcodes.append(['SHR'])
        elif opcode == '1d':
            opcodes.append(['SAR'])
        elif opcode == '20':
            opcodes.append(['SHA3'])
        elif opcode == '30':
            opcodes.append(['ADDRESS'])
        elif opcode == '31':
            opcodes.append(['BALANCE'])
        elif opcode == '32':
            opcodes.append(['ORIGIN'])
        elif opcode == '33':
            opcodes.append(['CALLER'])
        elif opcode == '34':
            opcodes.append(['CALLVALUE'])
        elif opcode == '35':
            opcodes.append(['CALLDATALOAD'])
        elif opcode == '36':
            opcodes.append(['CALLDATASIZE'])
        elif opcode == '37':
            opcodes.append(['CALLDATACOPY'])
        elif opcode == '38':
            opcodes.append(['CODESIZE'])
        elif opcode == '39':
            opcodes.append(['CODECOPY'])
        elif opcode == '3a':
            opcodes.append(['GASPRICE'])
        elif opcode == '3b':
            opcodes.append(['EXTCODESIZE'])
        elif opcode == '3c':
            opcodes.append(['EXTCODECOPY'])
        elif opcode == '3d':
            opcodes.append(['RETURNDATASIZE'])
        elif opcode == '3e':
            opcodes.append(['RETURNDATACOPY'])
        elif opcode == '3f':
            opcodes.append(['EXTCODEHASH'])
        elif opcode == '40':
            opcodes.append(['BLOCKHASH'])
        elif opcode == '41':
            opcodes.append(['COINBASE'])
        elif opcode == '42':
            opcodes.append(['TIMESTAMP'])
        elif opcode == '43':
            opcodes.append(['NUMBER'])
        elif opcode == '44':
            opcodes.append(['DIFFICULTY'])
        elif opcode == '45':
            opcodes.append(['GASLIMIT'])
        elif opcode == '46':
            opcodes.append(['CHAINID'])
        elif opcode == '47':
            opcodes.append(['SELFBALANCE'])
        elif opcode == '50':
            opcodes.append(['POP'])
        elif opcode == '51':
            opcodes.append(['MLOAD'])
        elif opcode == '52':
            opcodes.append(['MSTORE'])
        elif opcode == '53':
            opcodes.append(['MSTORE8'])
        elif opcode == '54':
            opcodes.append(['SLOAD'])
        elif opcode == '55':
            opcodes.append(['SSTORE'])
        elif opcode == '56':
            opcodes.append(['JUMP'])
        elif opcode == '57':
            opcodes.append(['JUMPI'])
        elif opcode == '58':
            opcodes.append(['PC'])
        elif opcode == '59':
            opcodes.append(['MSIZE'])
        elif opcode == '5a':
            opcodes.append(['GAS'])
        elif opcode == '5b':
            opcodes.append(['JUMPDEST'])
        elif opcode == '5f':
            opcodes.append(['PUSH0'])
        elif opcode == '60' or opcode == '61' or opcode == '62' or opcode == '63' or opcode == '64' or \
            opcode == '65' or opcode == '66' or opcode == '67' or opcode == '68' or opcode == '69' or \
            opcode == '6a' or opcode == '6b' or opcode == '6c' or opcode == '6d' or opcode == '6e' or \
            opcode == '6f' or opcode == '70' or opcode == '71' or opcode == '72' or opcode == '73' or \
            opcode == '74' or opcode == '75' or opcode == '76' or opcode == '77' or opcode == '78' or \
            opcode == '79' or opcode == '7a' or opcode == '7b' or opcode == '7c' or opcode == '7d' or \
            opcode == '7e' or opcode == '7f':
            push_value_length = int(opcode, 16) - int('5f', 16)
            push_value = bytecode[i + 2:i + 2 + push_value_length * 2]
            params.append('0x' + push_value)
            opcodes.append(['PUSH' + str(push_value_length)] + params)
            i += push_value_length * 2
        elif opcode == '80' or opcode == '81' or opcode == '82' or opcode == '83' or opcode == '84' or \
            opcode == '85' or opcode == '86' or opcode == '87' or opcode == '88' or opcode == '89' or \
            opcode == '8a' or opcode == '8b' or opcode == '8c' or opcode == '8d' or opcode == '8e' or \
            opcode == '8f':
            dup_index = int(opcode, 16) - int('7f', 16)
            opcodes.append(['DUP' + str(dup_index)])
        elif opcode == '90' or opcode == '91' or opcode == '92' or opcode == '93' or opcode == '94' or \
            opcode == '95' or opcode == '96' or opcode == '97' or opcode == '98' or opcode == '99' or \
            opcode == '9a' or opcode == '9b' or opcode == '9c' or opcode == '9d' or opcode == '9e' or \
            opcode == '9f':
            swap_index = int(opcode, 16) - int('8f', 16)
            opcodes.append(['SWAP', str(swap_index)])
        elif opcode == 'a0' or opcode == 'a1' or opcode == 'a2' or opcode == 'a3' or opcode == 'a4':
            log_index = int(opcode, 16) - int('9f', 16)
            opcodes.append(['LOG', str(log_index)])
        elif opcode == 'f0':
            opcodes.append(['CREATE'])
        elif opcode == 'f1':
            opcodes.append(['CALL'])
        elif opcode == 'f2':
            opcodes.append(['CALLCODE'])
        elif opcode == 'f3':
            opcodes.append(['RETURN'])
        elif opcode == 'f4':
            opcodes.append(['DELEGATECALL'])
        elif opcode == 'f5':
            opcodes.append(['CREATE2'])
        elif opcode == 'fa':
            opcodes.append(['STATICCALL'])
        elif opcode == 'fd':
            opcodes.append(['REVERT'])
        elif opcode == 'fe':
            opcodes.append(['INVALID'])
        elif opcode == 'ff':
            opcodes.append(['SUICIDE'])
        else:
            opcodes.append(['UNKNOWN'])

        i += 2

    return opcodes
